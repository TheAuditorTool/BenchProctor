// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("registry-service")
export class CollectSchedule {
  @Post("collectSchedule")
  async collectSchedule(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(subtitle);
    const persona: string = readInput();
    childProcess.execFile("echo", [String(persona)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
