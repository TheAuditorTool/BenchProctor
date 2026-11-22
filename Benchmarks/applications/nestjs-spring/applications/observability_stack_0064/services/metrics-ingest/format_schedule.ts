// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("metrics-ingest")
export class FormatSchedule {
  @Post("formatSchedule")
  async formatSchedule(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers["user-agent"] as string) || "";
    const gauge = tagline != null ? tagline : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(gauge));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const cohort = _parsed.data;
    childProcess.exec("echo " + cohort, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
