// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("capture-service")
export class SummarizeManifest {
  @Post("summarizeManifest")
  async summarizeManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.field as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const remittance: string = readInput();
    childProcess.execSync("echo " + remittance);
    return { created: true };
  }
}
