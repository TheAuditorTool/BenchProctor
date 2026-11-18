// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("ledger-sync")
export class ArchiveIndex {
  @Post("archiveIndex")
  async archiveIndex(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const arrears: string = readInput();
    childProcess.execSync("echo " + arrears);
    return { created: true };
  }
}
