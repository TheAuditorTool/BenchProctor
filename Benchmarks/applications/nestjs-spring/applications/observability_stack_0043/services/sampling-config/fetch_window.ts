// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sampling-config")
export class FetchWindow {
  @Post("fetchWindow")
  async fetchWindow(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    if (!/^(asc|desc|name|created)$/.test(String(gauge))) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    childProcess.execSync("echo " + cohort);
    return { created: true };
  }
}
