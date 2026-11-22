// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("bounce-handler")
export class AuditLedger {
  @Post("auditLedger")
  async auditLedger(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const bulletin: string = readInput();
    childProcess.execFile("echo", [String(bulletin)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
