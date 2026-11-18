// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("knowledge-index")
export class SummarizeCheckpoint {
  @Post("summarizeCheckpoint")
  async summarizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const inquiry = Buffer.from(note, "hex").toString();
    if (!["ls", "cat", "date", "whoami"].includes(inquiry)) { throw new ForbiddenException({error:'forbidden'}); }
    const grievance = inquiry;
    childProcess.execSync("echo " + grievance);
    return { created: true };
  }
}
