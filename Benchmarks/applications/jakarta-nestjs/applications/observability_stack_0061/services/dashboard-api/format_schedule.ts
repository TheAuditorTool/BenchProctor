// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("dashboard-api")
export class FormatSchedule {
  @Post("formatSchedule")
  async formatSchedule(@Req() req: Request): Promise<unknown> {
    const headline = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return headline; } };
    const cohort = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(cohort))) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
    return fileContent;
  }
}
