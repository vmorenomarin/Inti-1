
import multiprocessing as mp
import psutil


ma_obj = None
def process_wrapper(chunkStart, chunkSize):
    """
    wrapper to execute the function outside on the class,
    this trick is required for the module multiprocessing
    to avoid seralization problems  
    """
    global ma_obj 
    return ma_obj.process_wrapper(chunkStart, chunkSize)

def MAMagExecutor(obj,max_threads=None):
    """
    Function to call the parallel insertion of data by chunks
    using multiprocessing module.
    Keyword arguments:
    obj -- Object from class MAMagBase
    max_threads -- total number processors to use in parallel
    """
    global ma_obj
    ma_obj = obj
    if max_threads is None:
        jobs = psutil.cpu_count()
    else:
        jobs = max_threads

    pool = mp.Pool(max_threads)
    jobs = []


    #create jobs
    counter=0
    for chunkStart,chunkSize in obj.chunkify():
        jobs.append(pool.apply_async(process_wrapper,[chunkStart,chunkSize]) )
        counter=counter+1
        if counter%10==0:
            print(counter)

    #wait for all jobs to finish
    for job in jobs:
        job.get()

    #clean up
    pool.close()
