// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metrics-ingest")
export class ResolveWindow {
  @Post("resolveWindow")
  async resolveWindow(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(note);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(cohort)) { throw new BadRequestException({error:"invalid"}); }
    const gauge = cohort;
    fs.writeFileSync("/var/uploads/" + gauge, "data");
    return { created: true };
  }
}
