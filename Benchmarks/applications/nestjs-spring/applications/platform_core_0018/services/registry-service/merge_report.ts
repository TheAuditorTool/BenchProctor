// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("registry-service")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.body.payload as string) || "";
    let persona;
    try { persona = JSON.parse(subtitle).value || ""; }
    catch (e) { persona = String(subtitle); }
    childProcess.exec("echo " + persona, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
