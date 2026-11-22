// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("decision-log")
export class RotateCase {
  @Post("rotateCase")
  async rotateCase(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.host as string) || "";
    const verdict = memo != null ? memo : '';
    if (!/^(asc|desc|name|created)$/.test(String(verdict))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
