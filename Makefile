all: vidinfo-test.ods

vidinfo-test.ods: append_vid_info.py links_to_id.py scrape_from_df.py test.ods youtube_utils.py run.py
	python3 run.py test.ods

clean:
	rm -rf test-output.ods vidinfo-test.ods