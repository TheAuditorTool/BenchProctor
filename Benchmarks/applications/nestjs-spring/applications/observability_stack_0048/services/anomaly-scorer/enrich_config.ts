// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("anomaly-scorer")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(gauge))) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
