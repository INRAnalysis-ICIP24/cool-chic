> schedule.sh

for dist_fn in "mse:1.0" "log_cosh:1.0+ssim:0.01"
do        
    for lambda in "0.0001" "0.0005" "0.004" "0.02"
    do
        for file in test_images/clic2020/*
        do        
            basename=$(basename $file)
            image_id=${basename%.*}

            log_file="logs/${config_id}_$i.txt"
            echo "./samples/run_generic.sh test_images/clic2020/${image_id}.png $lambda \"results/cool-chic-v1/clic2020/${dist_fn}/${lambda}/${image_id}/\" \"$dist_fn\" > "\"logs/${dist_fn}_${lambda}_${image_id}.txt\"" 2>&1" >> schedule.sh
        done
    done
done