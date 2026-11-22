// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("revision-store")
export class SaveRevision {
  @Post("saveRevision")
  async saveRevision(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.publishing_payload || "";
    if (!/^(asc|desc|name|created)$/.test(String(transcript))) { throw new BadRequestException({error:"invalid"}); }
    const addendum = transcript;
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
