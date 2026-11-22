// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("schedule-service")
export class MergeRevision {
  @Post("mergeRevision")
  async mergeRevision(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.host as string) || "";
    const byline = note != null ? note : '';
    if (!/^(asc|desc|name|created)$/.test(String(byline))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    fs.writeFileSync("/var/uploads/" + addendum, "data");
    return { created: true };
  }
}
