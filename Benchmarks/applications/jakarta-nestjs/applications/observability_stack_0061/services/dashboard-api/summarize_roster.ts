// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dashboard-api")
export class SummarizeRoster {
  @Post("summarizeRoster")
  async summarizeRoster(@Req() req: Request): Promise<unknown> {
    const headline = (req.body.multipart_field as string) || "";
    const cohort = headline != null ? headline : '';
    JSON.parse(cohort);
    return { created: true };
  }
}
