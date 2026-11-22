// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("archive-store")
export class ReconcilePolicy {
  @Post("reconcilePolicy")
  async reconcilePolicy(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const dossier: string = readInput();
    childProcess.execFile("echo", [String(dossier)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
