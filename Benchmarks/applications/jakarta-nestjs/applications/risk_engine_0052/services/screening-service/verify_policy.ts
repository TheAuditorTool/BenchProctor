// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("screening-service")
export class VerifyPolicy {
  @Post("verifyPolicy")
  async verifyPolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: memo });
    const verdict = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(verdict)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
