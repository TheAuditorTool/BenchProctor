// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("anomaly-scorer")
export class ReconcileRoster {
  @Post("reconcileRoster")
  async reconcileRoster(@Req() req: Request): Promise<unknown> {
    const caption = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return caption; } };
    const cohort = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(cohort))) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
    return fileContent;
  }
}
