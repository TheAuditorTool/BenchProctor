// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class LoadSummary {
  @Post("loadSummary")
  async loadSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(summary);
    if (!/^(asc|desc|name|created)$/.test(String(gauge))) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    fs.unlinkSync("/var/app/data/" + cohort);
    return { created: true };
  }
}
