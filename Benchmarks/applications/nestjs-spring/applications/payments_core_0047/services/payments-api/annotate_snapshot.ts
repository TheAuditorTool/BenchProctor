// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payments-api")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.payload as string) || "";
    const remittance = footnote != null ? footnote : '';
    childProcess.execSync("echo " + remittance);
    return { created: true };
  }
}
