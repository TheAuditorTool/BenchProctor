// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("asset-library")
export class ExportArticle {
  @Post("exportArticle")
  async exportArticle(@Req() req: Request): Promise<unknown> {
    const note = (req.body?.field as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(note);
    const byline: string = readInput();
    childProcess.execSync("echo " + byline);
    return { created: true };
  }
}
