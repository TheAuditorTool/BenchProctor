// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class AnnotateManifest {
  @Post("annotateManifest")
  async annotateManifest(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(snippet);
    const montage: string = readInput();
    childProcess.execFile("echo", [String(montage)], (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
