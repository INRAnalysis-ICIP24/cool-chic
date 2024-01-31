> schedule.sh

# for dist_fn in "mse:1.0" "log_cosh:1.0" "l1:1.0" "l1:0.8+ssim:0.2" "log_cosh:1.0+ssim:0.01"
for dist_fn in "mse:1.0"
do        
    # for lambda in "0.002" "0.005" "0.006" "0.007" "0.008" "0.01" "0.012"
    for lambda in "0.002" "0.001"
    do
        for image_id in 11 # {1..24}
        do        
            log_file="logs/${config_id}_$i.txt"
            echo "./samples/run_generic.sh test_images/kodak/${image_id}.png $lambda \"results/cool-chic-v2/kodak/${dist_fn}/${lambda}/${image_id}/\" \"$dist_fn\" " >> schedule.sh
            # > "\"logs/${dist_fn}_${lambda}_${image_id}.txt\"" 2>&1" >> schedule.sh
        done
    done
done