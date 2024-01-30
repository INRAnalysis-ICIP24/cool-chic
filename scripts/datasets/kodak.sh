# > schedule.sh

# for dist_fn in "mse:1.0" "l1:1.0" "log_cosh:1.0+ssim:0.01" "l1:0.8+ssim:0.2" 
for dist_fn in "l1:1.0"
do        
    # for lambda in "0.0001" "0.0005" "0.004" "0.02"
    # for lambda in "0.005" "0.007"
    # for lambda in "0.01" "0.012"
    # for lambda in "0.08" "0.1" "0.12"
    for lambda in "0.001" "0.002"     
    do
        for image_id in 11
        # for image_id in {1..24}
        do        
            log_file="logs/${config_id}_$i.txt"
            echo "./samples/run_generic.sh test_images/kodak/${image_id}.png $lambda \"results/cool-chic-v2/kodak/${dist_fn}/${lambda}/${image_id}/\" \"$dist_fn\" " >> schedule.sh
            # > "\"logs/${dist_fn}_${lambda}_${image_id}.txt\"" 2>&1" >> schedule.sh
        done
    done
done