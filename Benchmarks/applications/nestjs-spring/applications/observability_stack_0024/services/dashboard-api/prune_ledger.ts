// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dashboard-api")
export class PruneLedger {
  @Post("pruneLedger")
  async pruneLedger(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(summary);
    return "<div>" + cohort + "</div>";
  }
}
