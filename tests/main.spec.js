import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://5controls.com/');
  await page.getByRole('button', { name: 'Yes, I agree' }).click();
  await page.locator('#mean-yearly-value').click();
  await page.locator('#cost-downtime-value').click();
  await page.locator('#cost-downtime-value').click();
  await page.locator('#cost-downtime-value').click();
  await page.locator('#cost-downtime-value').click();
  await page.locator('#mean-yearly-value').click();
  await page.locator('#downtime-hours-value').click();
  await page.locator('#downtime-value').click();
  await page.locator('#downtime-value').click();
  await page.locator('#downtime-value').click();
  await page.locator('#downtime-value').click();
  await page.locator('#downtime-value').click();
  await page.getByRole('link', { name: 'Go to slide 3' }).click();
  await page.getByRole('link', { name: 'Go to slide 4' }).click();
  await page.getByText('Suddenly run out of stock? Our min/MAX system ensures that the stock level is al').click();
  await page.locator('#contact').click();
  await page.getByRole('link', { name: 'free trial' }).click();
  await page.screenshot({path: 'test-results/test.jpg'})
});