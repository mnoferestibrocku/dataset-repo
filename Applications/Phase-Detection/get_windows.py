from tqdm import tqdm
import math

syscall_list = ['unknown', 'clone', 'execve', 'read', 'write', 'open', 'close', 'newstat', 'newfstat', 'newlstat', 'poll', 'lseek', 'mmap', 'mprotect', 'munmap', 'brk', 'rt_sigaction', 'rt_sigprocmask', 'ioctl', 'pread64', 'pwrite64', 'readv', 'writev', 'access', 'pipe', 'select', 'sched_yield', 'mremap', 'msync', 'mincore', 'madvise', 'shmget', 'shmat', 'shmctl', 'dup', 'dup2', 'pause', 'nanosleep', 'getitimer', 'alarm', 'setitimer', 'getpid', 'sendfile64', 'socket', 'connect', 'accept', 'sendto', 'recvfrom', 'sendmsg', 'recvmsg', 'shutdown', 'bind', 'listen', 'getsockname', 'getpeername', 'socketpair', 'setsockopt', 'getsockopt', 'exit', 'wait4', 'kill', 'newuname', 'semget', 'semop', 'semctl', 'shmdt', 'msgget', 'msgsnd', 'msgrcv', 'msgctl', 'fcntl', 'flock', 'fsync', 'fdatasync', 'truncate', 'ftruncate', 'getdents', 'getcwd', 'chdir', 'fchdir', 'rename', 'mkdir', 'rmdir', 'creat', 'link', 'unlink', 'symlink', 'readlink', 'chmod', 'fchmod', 'chown', 'fchown', 'lchown', 'umask', 'gettimeofday', 'getrlimit', 'getrusage', 'sysinfo', 'times', 'ptrace', 'getuid', 'syslog', 'getgid', 'setuid', 'setgid', 'geteuid', 'getegid', 'setpgid', 'getppid', 'getpgrp', 'setsid', 'setreuid', 'setregid', 'getgroups', 'setgroups', 'setresuid', 'getresuid', 'setresgid', 'getresgid', 'getpgid', 'setfsuid', 'setfsgid', 'getsid', 'capget', 'capset', 'rt_sigpending', 'rt_sigtimedwait', 'rt_sigqueueinfo', 'rt_sigsuspend', 'sigaltstack', 'utime', 'mknod', 'personality', 'ustat', 'statfs', 'fstatfs', 'sysfs', 'getpriority', 'setpriority', 'sched_setparam', 'sched_getparam', 'sched_setscheduler', 'sched_getscheduler', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_rr_get_interval', 'mlock', 'munlock', 'mlockall', 'munlockall', 'vhangup', 'modify_ldt', 'pivot_root', 'sysctl', 'prctl', 'arch_prctl', 'adjtimex', 'setrlimit', 'chroot', 'sync', 'acct', 'settimeofday', 'mount', 'umount', 'swapon', 'swapoff', 'reboot', 'sethostname', 'setdomainname', 'ioperm', 'init_module', 'delete_module', 'quotactl', 'gettid', 'readahead', 'setxattr', 'lsetxattr', 'fsetxattr', 'getxattr', 'lgetxattr', 'fgetxattr', 'listxattr', 'llistxattr', 'flistxattr', 'removexattr', 'lremovexattr', 'fremovexattr', 'tkill', 'time', 'futex', 'sched_setaffinity', 'sched_getaffinity', 'io_setup', 'io_destroy', 'io_getevents', 'io_submit', 'io_cancel', 'lookup_dcookie', 'epoll_create', 'remap_file_pages', 'getdents64', 'set_tid_address', 'restart_syscall', 'semtimedop', 'fadvise64', 'timer_create', 'timer_settime', 'timer_gettime', 'timer_getoverrun', 'timer_delete', 'clock_settime', 'clock_gettime', 'clock_getres', 'clock_nanosleep', 'exit_group', 'epoll_wait', 'epoll_ctl', 'tgkill', 'utimes', 'mbind', 'set_mempolicy', 'get_mempolicy', 'mq_open', 'mq_unlink', 'mq_timedsend', 'mq_timedreceive', 'mq_notify', 'mq_getsetattr', 'kexec_load', 'waitid', 'add_key', 'request_key', 'keyctl', 'ioprio_set', 'ioprio_get', 'inotify_init', 'inotify_add_watch', 'inotify_rm_watch', 'migrate_pages', 'openat', 'mkdirat', 'mknodat', 'fchownat', 'futimesat', 'newfstatat', 'unlinkat', 'renameat', 'linkat', 'symlinkat', 'readlinkat', 'fchmodat', 'faccessat', 'pselect6', 'ppoll', 'unshare', 'set_robust_list', 'get_robust_list', 'splice', 'tee', 'sync_file_range', 'vmsplice', 'move_pages', 'utimensat', 'epoll_pwait', 'signalfd', 'timerfd_create', 'eventfd', 'fallocate', 'timerfd_settime', 'timerfd_gettime', 'accept4', 'signalfd4', 'eventfd2', 'epoll_create1', 'dup3', 'pipe2', 'inotify_init1', 'preadv', 'pwritev', 'rt_tgsigqueueinfo', 'perf_event_open', 'recvmmsg', 'fanotify_init', 'fanotify_mark', 'prlimit64', 'name_to_handle_at', 'open_by_handle_at', 'clock_adjtime', 'syncfs', 'sendmmsg', 'setns', 'getcpu', 'process_vm_readv', 'process_vm_writev', 'kcmp', 'finit_module', 'sched_setattr', 'sched_getattr', 'renameat2', 'seccomp', 'getrandom', 'memfd_create', 'kexec_file_load', 'bpf', 'userfaultfd', 'membarrier', 'mlock2', 'copy_file_range', 'preadv2', 'pwritev2', 'pkey_mprotect', 'pkey_alloc', 'pkey_free', 'compat_rt_sigaction', 'compat_ioctl', 'compat_readv', 'compat_writev', 'compat_recvfrom', 'compat_sendmsg', 'compat_recvmsg', 'compat_ptrace', 'compat_rt_sigpending', 'compat_rt_sigtimedwait', 'compat_rt_sigqueueinfo', 'compat_sigaltstack', 'compat_timer_create', 'compat_mq_notify', 'compat_kexec_load', 'compat_waitid', 'compat_set_robust_list', 'compat_get_robust_list', 'compat_vmsplice', 'compat_move_pages', 'compat_preadv64', 'compat_pwritev64', 'compat_rt_tgsigqueueinfo', 'compat_recvmmsg', 'compat_sendmmsg', 'compat_process_vm_readv', 'compat_process_vm_writev', 'compat_setsockopt', 'compat_getsockopt', 'compat_io_setup', 'compat_io_submit']
module_options = ['other', 'fs', 'arch', 'mm', 'kernel', 'ipc', 'net', 'security', 'block', 'drivers']
syscall_mod_dict = {'other': 'other', 'read': 'fs', 'write': 'fs', 'open': 'fs', 'close': 'fs', 'newstat': 'fs', 'newfstat': 'fs', 'newlstat': 'fs', 'poll': 'fs', 'lseek': 'fs', 'mmap': 'arch', 'mprotect': 'mm', 'munmap': 'mm', 'brk': 'mm', 'rt_sigaction': 'kernel', 'rt_sigprocmask': 'kernel', 'ioctl': 'fs', 'pread64': 'fs', 'pwrite64': 'fs', 'readv': 'fs', 'writev': 'fs', 'access': 'fs', 'pipe': 'fs', 'select': 'fs', 'sched_yield': 'kernel', 'mremap': 'mm', 'msync': 'mm', 'mincore': 'mm', 'madvise': 'mm', 'shmget': 'ipc', 'shmat': 'ipc', 'shmctl': 'ipc', 'dup': 'fs', 'dup2': 'fs', 'pause': 'kernel', 'nanosleep': 'kernel', 'getitimer': 'kernel', 'alarm': 'kernel', 'setitimer': 'kernel', 'getpid': 'kernel', 'sendfile64': 'fs', 'socket': 'net', 'connect': 'net', 'accept': 'net', 'sendto': 'net', 'recvfrom': 'net', 'sendmsg': 'net', 'recvmsg': 'net', 'shutdown': 'net', 'bind': 'net', 'listen': 'net', 'getsockname': 'net', 'getpeername': 'net', 'socketpair': 'net', 'setsockopt': 'net', 'getsockopt': 'net', 'exit': 'kernel', 'wait4': 'kernel', 'kill': 'kernel', 'newuname': 'kernel', 'semget': 'ipc', 'semop': 'ipc', 'semctl': 'ipc', 'shmdt': 'ipc', 'msgget': 'ipc', 'msgsnd': 'ipc', 'msgrcv': 'ipc', 'msgctl': 'ipc', 'fcntl': 'fs', 'flock': 'fs', 'fsync': 'fs', 'fdatasync': 'fs', 'truncate': 'fs', 'ftruncate': 'fs', 'getdents': 'fs', 'getcwd': 'fs', 'chdir': 'fs', 'fchdir': 'fs', 'rename': 'fs', 'mkdir': 'fs', 'rmdir': 'fs', 'creat': 'fs', 'link': 'fs', 'unlink': 'fs', 'symlink': 'fs', 'readlink': 'fs', 'chmod': 'fs', 'fchmod': 'fs', 'chown': 'fs', 'fchown': 'fs', 'lchown': 'fs', 'umask': 'kernel', 'gettimeofday': 'kernel', 'getrlimit': 'kernel', 'getrusage': 'kernel', 'sysinfo': 'kernel', 'times': 'kernel', 'ptrace': 'kernel', 'getuid': 'kernel', 'syslog': 'kernel', 'getgid': 'kernel', 'setuid': 'kernel', 'setgid': 'kernel', 'geteuid': 'kernel', 'getegid': 'kernel', 'setpgid': 'kernel', 'getppid': 'kernel', 'getpgrp': 'kernel', 'setsid': 'kernel', 'setreuid': 'kernel', 'setregid': 'kernel', 'getgroups': 'kernel', 'setgroups': 'kernel', 'setresuid': 'kernel', 'getresuid': 'kernel', 'setresgid': 'kernel', 'getresgid': 'kernel', 'getpgid': 'kernel', 'setfsuid': 'kernel', 'setfsgid': 'kernel', 'getsid': 'kernel', 'capget': 'kernel', 'capset': 'kernel', 'rt_sigpending': 'kernel', 'rt_sigtimedwait': 'kernel', 'rt_sigqueueinfo': 'kernel', 'rt_sigsuspend': 'kernel', 'sigaltstack': 'kernel', 'utime': 'fs', 'mknod': 'fs', 'personality': 'kernel', 'ustat': 'fs', 'statfs': 'fs', 'fstatfs': 'fs', 'sysfs': 'fs', 'getpriority': 'kernel', 'setpriority': 'kernel', 'sched_setparam': 'kernel', 'sched_getparam': 'kernel', 'sched_setscheduler': 'kernel', 'sched_getscheduler': 'kernel', 'sched_get_priority_max': 'kernel', 'sched_get_priority_min': 'kernel', 'sched_rr_get_interval': 'kernel', 'mlock': 'mm', 'munlock': 'mm', 'mlockall': 'mm', 'munlockall': 'mm', 'vhangup': 'fs', 'modify_ldt': 'other', 'pivot_root': 'fs', 'sysctl': 'kernel', 'prctl': 'kernel', 'arch_prctl': 'other', 'adjtimex': 'kernel', 'setrlimit': 'kernel', 'chroot': 'fs', 'sync': 'fs', 'acct': 'kernel', 'settimeofday': 'kernel', 'mount': 'fs', 'umount': 'fs', 'swapon': 'mm', 'swapoff': 'mm', 'reboot': 'kernel', 'sethostname': 'kernel', 'setdomainname': 'kernel', 'ioperm': 'other', 'init_module': 'kernel', 'delete_module': 'kernel', 'quotactl': 'fs', 'gettid': 'kernel', 'readahead': 'mm', 'setxattr': 'fs', 'lsetxattr': 'fs', 'fsetxattr': 'fs', 'getxattr': 'fs', 'lgetxattr': 'fs', 'fgetxattr': 'fs', 'listxattr': 'fs', 'llistxattr': 'fs', 'flistxattr': 'fs', 'removexattr': 'fs', 'lremovexattr': 'fs', 'fremovexattr': 'fs', 'tkill': 'kernel', 'time': 'kernel', 'futex': 'kernel', 'sched_setaffinity': 'kernel', 'sched_getaffinity': 'kernel', 'io_setup': 'fs', 'io_destroy': 'fs', 'io_getevents': 'fs', 'io_submit': 'fs', 'io_cancel': 'fs', 'lookup_dcookie': 'fs', 'epoll_create': 'fs', 'remap_file_pages': 'mm', 'getdents64': 'fs', 'set_tid_address': 'kernel', 'restart_syscall': 'kernel', 'semtimedop': 'ipc', 'fadvise64': 'mm', 'timer_create': 'kernel', 'timer_settime': 'kernel', 'timer_gettime': 'kernel', 'timer_getoverrun': 'kernel', 'timer_delete': 'kernel', 'clock_settime': 'kernel', 'clock_gettime': 'kernel', 'clock_getres': 'kernel', 'clock_nanosleep': 'kernel', 'exit_group': 'kernel', 'epoll_wait': 'fs', 'epoll_ctl': 'fs', 'tgkill': 'kernel', 'utimes': 'fs', 'mbind': 'mm', 'set_mempolicy': 'mm', 'get_mempolicy': 'mm', 'mq_open': 'ipc', 'mq_unlink': 'ipc', 'mq_timedsend': 'ipc', 'mq_timedreceive': 'ipc', 'mq_notify': 'ipc', 'mq_getsetattr': 'ipc', 'kexec_load': 'kernel', 'waitid': 'kernel', 'add_key': 'security', 'request_key': 'security', 'keyctl': 'security', 'ioprio_set': 'block', 'ioprio_get': 'block', 'inotify_init': 'fs', 'inotify_add_watch': 'fs', 'inotify_rm_watch': 'fs', 'migrate_pages': 'mm', 'openat': 'fs', 'mkdirat': 'fs', 'mknodat': 'fs', 'fchownat': 'fs', 'futimesat': 'fs', 'newfstatat': 'fs', 'unlinkat': 'fs', 'renameat': 'fs', 'linkat': 'fs', 'symlinkat': 'fs', 'readlinkat': 'fs', 'fchmodat': 'fs', 'faccessat': 'fs', 'pselect6': 'fs', 'ppoll': 'fs', 'unshare': 'kernel', 'set_robust_list': 'kernel', 'get_robust_list': 'kernel', 'splice': 'fs', 'tee': 'fs', 'sync_file_range': 'fs', 'vmsplice': 'fs', 'move_pages': 'mm', 'utimensat': 'fs', 'epoll_pwait': 'fs', 'signalfd': 'fs', 'timerfd_create': 'fs', 'eventfd': 'fs', 'fallocate': 'fs', 'timerfd_settime': 'fs', 'timerfd_gettime': 'fs', 'accept4': 'net', 'signalfd4': 'fs', 'eventfd2': 'fs', 'epoll_create1': 'fs', 'dup3': 'fs', 'pipe2': 'fs', 'inotify_init1': 'fs', 'preadv': 'fs', 'pwritev': 'fs', 'rt_tgsigqueueinfo': 'kernel', 'perf_event_open': 'kernel', 'recvmmsg': 'net', 'fanotify_init': 'fs', 'fanotify_mark': 'fs', 'prlimit64': 'kernel', 'name_to_handle_at': 'fs', 'open_by_handle_at': 'fs', 'clock_adjtime': 'kernel', 'syncfs': 'fs', 'sendmmsg': 'net', 'setns': 'kernel', 'getcpu': 'kernel', 'process_vm_readv': 'mm', 'process_vm_writev': 'mm', 'kcmp': 'kernel', 'finit_module': 'kernel', 'sched_setattr': 'kernel', 'sched_getattr': 'kernel', 'renameat2': 'fs', 'seccomp': 'kernel', 'getrandom': 'drivers', 'memfd_create': 'mm', 'kexec_file_load': 'kernel', 'bpf': 'kernel', 'userfaultfd': 'fs', 'membarrier': 'kernel', 'mlock2': 'mm', 'copy_file_range': 'fs', 'preadv2': 'fs', 'pwritev2': 'fs', 'pkey_mprotect': 'mm', 'pkey_alloc': 'mm', 'pkey_free': 'mm', 'compat_rt_sigaction': 'other', 'compat_ioctl': 'other', 'compat_readv': 'other', 'compat_writev': 'other', 'compat_recvfrom': 'other', 'compat_sendmsg': 'other', 'compat_recvmsg': 'other', 'compat_ptrace': 'other', 'compat_rt_sigpending': 'other', 'compat_rt_sigtimedwait': 'other', 'compat_rt_sigqueueinfo': 'other', 'compat_sigaltstack': 'other', 'compat_timer_create': 'other', 'compat_mq_notify': 'other', 'compat_kexec_load': 'other', 'compat_waitid': 'other', 'compat_set_robust_list': 'other', 'compat_get_robust_list': 'other', 'compat_vmsplice': 'other', 'compat_move_pages': 'other', 'compat_preadv64': 'other', 'compat_pwritev64': 'other', 'compat_rt_tgsigqueueinfo': 'other', 'compat_recvmmsg': 'other', 'compat_sendmmsg': 'other', 'compat_process_vm_readv': 'other', 'compat_process_vm_writev': 'other', 'compat_setsockopt': 'other', 'compat_getsockopt': 'other', 'compat_io_setup': 'other', 'compat_io_submit': 'other'}

def duration_windows(events, timestamps, durations, window_size):
    if len(events) == 0:
        print("Not enough data")
        return [], []
    print("Window size of %d seconds" %(window_size))
    window = window_size*1e9
    dataset = []
    mod_dataset = []
    tracker = 0
    num_items = len(events)
    data_duration = timestamps[-1] - timestamps[0]
    num_vect = math.ceil(data_duration/window)
    for v in tqdm(range(num_vect)):
        temp = [0]*len(syscall_list)
        temp_mod = [0]*len(module_options)
        offset = v*window
        start = timestamps[0] + offset
        cutoff = start + window
        while tracker < num_items:
            e = events[tracker].replace("syscall_exit_", "").replace("syscall_entry_", "")
            if e in syscall_list and timestamps[tracker] >= start:
                if timestamps[tracker] <= cutoff:
                    temp[syscall_list.index(e)] += 1
                    if e in syscall_mod_dict.keys():
                        temp_mod[module_options.index(syscall_mod_dict[e])] += durations[tracker]
                    else:
                        temp_mod[module_options.index('other')] += durations[tracker]
                else:
                    break
            tracker += 1
        mod_dataset.append(temp_mod)
        dataset.append(temp)    
    return dataset, mod_dataset

def event_windows(events, durations, window_size):
    if len(events) == 0:
        print("Not enough data")
        return [], []
    
    print("Window size of %d events" %(window_size))
    items = [x.replace("syscall_exit_", "").replace("syscall_entry_", "") for x in events if x.replace("syscall_exit_", "").replace("syscall_entry_", "") in syscall_list]
    dataset = []
    mod_dataset = []
    tracker = 0
    num_items = len(items)
    while tracker < num_items:
        temp = [0]*len(syscall_list)
        temp_mod = [0]*len(module_options)
        for x in range(window_size):
            if tracker < num_items:
                temp[syscall_list.index(items[tracker])] += 1
                if items[tracker] in syscall_mod_dict.keys():
                    temp_mod[module_options.index(syscall_mod_dict[items[tracker]])] += durations[tracker]
                else: 
                    temp_mod[module_options.index('other')] += durations[tracker]
            tracker += 1   
        dataset.append(temp)
        mod_dataset.append(temp_mod)
    return dataset, mod_dataset

def duration_sliding_windows(events, timestamps, durations, window_size, step=0.75):
    if len(events) == 0:
        print("Not enough data")
        return [], []
    
    assert(step > 0 and step <= 1)
    print("Window size of %d seconds" %(window_size))
    window = window_size*1e9
    dataset = []
    mod_dataset = []
    tracker = 0
    num_items = len(events)
    data_duration = timestamps[-1] - timestamps[0]
    num_vect = math.ceil(data_duration/(window*step))
    for v in tqdm(range(num_vect)):
        temp = [0]*len(syscall_list)
        temp_mod = [0]*len(module_options)
        offset = v*math.floor(window*step)
        start = timestamps[0] + offset
        cutoff = start + window
        while tracker < num_items:
            e = events[tracker].replace("syscall_exit_", "").replace("syscall_entry_", "")
            if e in syscall_list and timestamps[tracker] >= start:
                if timestamps[tracker] <= cutoff:
                    temp[syscall_list.index(e)] += 1
                    if e in syscall_mod_dict.keys():
                        temp_mod[module_options.index(syscall_mod_dict[e])] += durations[tracker]
                    else: 
                        temp_mod[module_options.index('other')] += durations[tracker]
                else:
                    break
            tracker += 1

        dataset.append(temp)    
        mod_dataset.append(temp_mod)
    return dataset, mod_dataset

def event_sliding_windows(events, durations, window_size, step=0.75):
    if len(events) == 0:
        print("Not enough data")
        return [], []
    
    print("Window size of %d events" %(window_size))
    items = [x.replace("syscall_exit_", "").replace("syscall_entry_", "") for x in events if x.replace("syscall_exit_", "").replace("syscall_entry_", "") in syscall_list]
    dataset = []
    mod_dataset = []
    tracker = 0
    num_items = len(items)
    while tracker < num_items:
        temp = [0]*len(syscall_list)
        temp_mod = [0]*len(module_options)
        for x in range(window_size):
            if tracker < num_items:
                temp[syscall_list.index(items[tracker])] += 1
                if items[tracker] in syscall_mod_dict.keys():
                    temp_mod[module_options.index(syscall_mod_dict[items[tracker]])] += durations[tracker]
                else: 
                    temp_mod[module_options.index('other')] += durations[tracker]
            tracker += 1  
        tracker = tracker - int(window_size*(1-step)) 
        dataset.append(temp)
        mod_dataset.append(temp_mod)
    return dataset, mod_dataset

def save_data(vectors, outpath):
    outpath = outpath.split("/")
    outpath[-1] = "data_" + outpath[-1]
    outpath = "/".join(outpath)
    csv_out = open(outpath, 'w')
    if len(vectors) > 0:
        for x in range(len(vectors)-1):
            csv_out.write(','.join([str(s) for s in vectors[x]])+'\n')
        csv_out.write(','.join([str(s) for s in vectors[-1]]))
    csv_out.close()

def read_dataset(path):
    d = open(path, 'r')
    data = d.readlines()
    d.close()
    data = [[int(x) for x in d.strip().split(",")] for d in data]
    return data
