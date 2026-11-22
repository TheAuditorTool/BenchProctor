// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: note });
    const cohort = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    fs.writeFileSync("/var/uploads/" + gauge, "data");
    return { created: true };
  }
}
