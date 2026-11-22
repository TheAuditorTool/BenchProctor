// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("address-validator")
export class ExportSummary {
  @Post("exportSummary")
  async exportSummary(@Req() req: Request): Promise<unknown> {
    const quotation = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(quotation);
    const parcel: string = readInput();
    childProcess.execFile("echo", [String(parcel)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
