// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metrics-ingest")
export class SummarizeDigest {
  @Post("summarizeDigest")
  async summarizeDigest(@Req() req: Request): Promise<unknown> {
    const caption = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return caption; } };
    const gauge = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(gauge))) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    const fileContent = fs.readFileSync("/var/app/data/" + cohort, "utf8");
    return fileContent;
  }
}
