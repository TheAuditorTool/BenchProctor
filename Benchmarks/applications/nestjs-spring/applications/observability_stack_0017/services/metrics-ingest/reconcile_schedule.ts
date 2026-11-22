// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("metrics-ingest")
export class ReconcileSchedule {
  @Post("reconcileSchedule")
  async reconcileSchedule(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["x-forwarded-for"] as string) || "";
    const cohort = note != null ? note : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    return "<div>" + gauge + "</div>";
  }
}
