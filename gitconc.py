{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"gitconc.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyNCa/htO/54cldWYH9JSWfB"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"E9rtPF89xUnQ","executionInfo":{"status":"ok","timestamp":1661244129704,"user_tz":-540,"elapsed":2637,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"48fd0221-2db7-4fbb-e355-16c158a44c27"},"outputs":[{"output_type":"stream","name":"stdout","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"]}],"source":["from google.colab import drive\n","drive.mount('/content/drive')"]},{"cell_type":"code","source":["!git config --global user.name 'jjobis'\n","!git config --global user.email 'whwnsgh427@gmail.com'\n","!git config --global user.password '03427chojun@'"],"metadata":{"id":"t0qLZFbv3cpJ","executionInfo":{"status":"ok","timestamp":1661245402612,"user_tz":-540,"elapsed":736,"user":{"displayName":"조준호","userId":"14774737217702745248"}}},"execution_count":35,"outputs":[]},{"cell_type":"code","source":["GIT_token = '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'\n","GIT_username = 'jjobis'\n","GIT_repo = 'python'\n","GIT_path = \"https://\" + GIT_token + '@github.com/' + GIT_username + '/' + GIT_repo + '.git'\n","print(GIT_path)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"GarzE2maxkTg","executionInfo":{"status":"ok","timestamp":1661245403004,"user_tz":-540,"elapsed":3,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"806c11a9-2155-44e2-8302-5a7668633da8"},"execution_count":36,"outputs":[{"output_type":"stream","name":"stdout","text":["https://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@github.com/jjobis/python.git\n"]}]},{"cell_type":"code","source":["from os.path import join\n","proj_path = '/content/drive/MyDrive/Colab Notebooks/'\n","%cd '{proj_path}'\n","!git clone '{GIT_path}'"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"r7XGPjUnzNhH","executionInfo":{"status":"ok","timestamp":1661245404378,"user_tz":-540,"elapsed":394,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"08745bcf-f182-4fe6-9220-742250b0d96e"},"execution_count":37,"outputs":[{"output_type":"stream","name":"stdout","text":["/content/drive/MyDrive/Colab Notebooks\n","fatal: destination path 'python' already exists and is not an empty directory.\n"]}]},{"cell_type":"code","source":["%cd {GIT_repo}"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"AtGrrXjMztyU","executionInfo":{"status":"ok","timestamp":1661245405657,"user_tz":-540,"elapsed":2,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"669c9f44-5e9b-449c-891c-aff7720f20a0"},"execution_count":38,"outputs":[{"output_type":"stream","name":"stdout","text":["/content/drive/MyDrive/Colab Notebooks/python\n"]}]},{"cell_type":"code","source":["%ls"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"-wRNnLiG2y2X","executionInfo":{"status":"ok","timestamp":1661245406755,"user_tz":-540,"elapsed":431,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"49a94d88-583f-40bd-8dc7-864fe8a9e159"},"execution_count":39,"outputs":[{"output_type":"stream","name":"stdout","text":["README.md  test01.py\n"]}]},{"cell_type":"code","source":["!git status"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"JUrtwajR4AJi","executionInfo":{"status":"ok","timestamp":1661245408020,"user_tz":-540,"elapsed":369,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"76a372ca-486c-47d7-f223-7b69f6bb7be7"},"execution_count":40,"outputs":[{"output_type":"stream","name":"stdout","text":["On branch main\n","Your branch is ahead of 'origin/main' by 1 commit.\n","  (use \"git push\" to publish your local commits)\n","\n","nothing to commit, working tree clean\n"]}]},{"cell_type":"code","source":["!git add --all\n","!git commit -m 'test01 push'\n","!git push origin main"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"oj6atYls3Mqv","executionInfo":{"status":"ok","timestamp":1661245437382,"user_tz":-540,"elapsed":858,"user":{"displayName":"조준호","userId":"14774737217702745248"}},"outputId":"f050a46f-6087-47f3-b65d-8751b3589576"},"execution_count":42,"outputs":[{"output_type":"stream","name":"stdout","text":["On branch main\n","Your branch is ahead of 'origin/main' by 1 commit.\n","  (use \"git push\" to publish your local commits)\n","\n","nothing to commit, working tree clean\n","To https://github.com/jjobis/python.git\n"," ! [rejected]        main -> main (fetch first)\n","error: failed to push some refs to 'https://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@github.com/jjobis/python.git'\n","hint: Updates were rejected because the remote contains work that you do\n","hint: not have locally. This is usually caused by another repository pushing\n","hint: to the same ref. You may want to first integrate the remote changes\n","hint: (e.g., 'git pull ...') before pushing again.\n","hint: See the 'Note about fast-forwards' in 'git push --help' for details.\n"]}]}]}