// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("member-directory")
export class RotateProfile {
  @Post("rotateProfile")
  async rotateProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const wording: string = parts.join(',');
    const reportSpec = jsYaml.load(String(wording), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
