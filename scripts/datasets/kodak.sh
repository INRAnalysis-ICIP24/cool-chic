> schedule.sh

for dist_fn in "mse:1.0" "l1:1.0" "l1:0.8 ssim:0.2"
do        
    for lambda in "0.0001" "0.0005" "0.004" "0.02"
    do
        for image_id in {1..24}
        do        
            log_file="logs/${config_id}_$i.txt"
            echo "./samples/run_generic.sh test_images/kodak/${image_id}.png $lambda \"results/cool-chic-v1/kodak/${dist_fn}/${lambda}/${image_id}/\" \"$dist_fn\" > "\"logs/${dist_fn}_${lambda}_${image_id}.txt\"" 2>&1" >> schedule.sh
        done
    done
done