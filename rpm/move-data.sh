#/bin/sh
old_dir="$HOME/.qmf"
new_dir="$HOME/.local/share/qmf"

if [ -d $old_dir -a ! -d $new_dir/database ]; then
    # try to  cope with something having created an empty directory at target
    rmdir $new_dir
    mv $old_dir $new_dir
fi

