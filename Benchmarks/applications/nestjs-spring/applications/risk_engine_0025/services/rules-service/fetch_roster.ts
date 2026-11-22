// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("rules-service")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(excerpt);
    const verdict: string = readInput();
    childProcess.execFile("echo", [String(verdict)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
