// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("payments-api")
export class PublishPolicy {
  @Post("publishPolicy")
  async publishPolicy(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const remittance: string = readInput();
    childProcess.execFile("echo", [String(remittance)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
