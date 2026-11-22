// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("preview-renderer")
export class AuditBatch {
  @Post("auditBatch")
  async auditBatch(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.field as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(heading);
    const addendum: string = readInput();
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
