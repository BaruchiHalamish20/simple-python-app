# GitHub Personal Access Token Setup Guide

This guide will help you create and configure the Personal Access Token (PAT) required for the CI/CD workflow to update the DevOps repository.

## Why is this needed?

The GitHub Actions workflow needs to:
1. Build and push Docker images (uses automatic `GITHUB_TOKEN` ✅)
2. Push image tag updates to the **DevOps repository** (requires `DEVOPS_REPO_TOKEN` ⚠️)

The automatic `GITHUB_TOKEN` only has permissions for the repository where the workflow runs. To push to another repository, you need a Personal Access Token.

## Step-by-Step Instructions

### 1. Create a Personal Access Token (PAT)

1. Go to GitHub and click your profile picture (top right)
2. Click **Settings**
3. Scroll down to **Developer settings** (bottom of left sidebar)
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Fill in the form:
   - **Note**: `DevOps Repo Access for CI/CD` (or any descriptive name)
   - **Expiration**: Choose your preferred expiration (90 days, 1 year, or no expiration)
   - **Select scopes**:
     - ✅ Check `repo` (this gives full control of private repositories)
7. Click **Generate token** at the bottom
8. **IMPORTANT**: Copy the token immediately! You won't be able to see it again.
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 2. Add Token to Repository Secrets

1. Go to your **simple-python-app** repository on GitHub
2. Click **Settings** (in the repository menu)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret** (green button)
5. Fill in:
   - **Name**: `DEVOPS_REPO_TOKEN` (exactly as shown, case-sensitive)
   - **Secret**: Paste the token you copied in step 1
6. Click **Add secret**

### 3. Verify the Setup

1. Go to the **Actions** tab in your repository
2. Find the latest workflow run (it probably failed with "Permission denied")
3. Click **Re-run all jobs** in the top right
4. The workflow should now complete successfully! ✅

## Troubleshooting

### "Permission denied to github-actions[bot]"
- The `DEVOPS_REPO_TOKEN` secret is not set or is invalid
- Double-check that you:
  - Created the token with `repo` scope
  - Added it with the exact name `DEVOPS_REPO_TOKEN`
  - The token hasn't expired

### "Bad credentials"
- The token might be invalid or expired
- Create a new token and update the secret

### Token Expiration
If you set an expiration date, remember to:
1. Create a new token before the old one expires
2. Update the `DEVOPS_REPO_TOKEN` secret with the new token

## Security Best Practices

✅ **DO:**
- Use a descriptive name for your token
- Set a reasonable expiration date (e.g., 90 days or 1 year)
- Delete tokens you're no longer using
- Use fine-grained tokens when they become generally available

❌ **DON'T:**
- Share your token publicly
- Commit the token to your repository
- Use the same token for multiple purposes
- Give more permissions than needed

## What Happens After Setup?

Once configured, your CI/CD workflow will:

1. ✅ Build Docker image
2. ✅ Push to GitHub Container Registry (`ghcr.io/baruchihalaish20/simple-python-app`)
3. ✅ Checkout DevOps repository (using `DEVOPS_REPO_TOKEN`)
4. ✅ Update image tags in environment configs
5. ✅ Commit and push changes to DevOps repo
6. ✅ ArgoCD detects changes and deploys automatically

---

**Need help?** Check the [README.md](README.md) for more information about the CI/CD pipeline.

