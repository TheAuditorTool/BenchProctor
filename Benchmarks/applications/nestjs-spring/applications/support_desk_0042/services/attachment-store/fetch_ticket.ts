// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("attachment-store")
export class FetchTicket {
  @Post("fetchTicket")
  async fetchTicket(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(blurb);
    const inquiry: string = readInput();
    childProcess.execFile("echo", [String(inquiry)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
