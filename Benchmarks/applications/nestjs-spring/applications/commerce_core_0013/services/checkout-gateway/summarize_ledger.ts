// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("checkout-gateway")
export class SummarizeLedger {
  @Post("summarizeLedger")
  async summarizeLedger(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(wording);
    const backorder: string = readInput();
    childProcess.execFile("echo", [String(backorder)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
