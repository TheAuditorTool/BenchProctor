// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class BuildSummary {
  @Post("buildSummary")
  async buildSummary(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(synopsis);
    return "<div>" + verdict + "</div>";
  }
}
