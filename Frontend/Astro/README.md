# Start

1. 初始化项目: `pnpm create astro@latest`
2. Integration: `pnpm astro add tailwind`
3. CI/CD with Github
	* create a github repo
	* configure native project
```bash
echo "# blog" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:Kaikaikaifang/blog.git
git push -u origin main
```