function mat_worker(in_dir, in_fn, out_fn)

% worker to manipulate a .mat file saved by python

disp('The worker is working!')

load([in_dir, in_fn]);

% we ASSUME that we loaded a and b - this depends on the driving program

% square them
aa = a.*a;

bb = b.*b;

% save to disk
save([in_dir, out_fn], 'aa', 'bb');
