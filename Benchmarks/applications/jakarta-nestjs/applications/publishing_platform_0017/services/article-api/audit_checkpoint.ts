// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("article-api")
export class AuditCheckpoint {
  @Post("auditCheckpoint")
  async auditCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
