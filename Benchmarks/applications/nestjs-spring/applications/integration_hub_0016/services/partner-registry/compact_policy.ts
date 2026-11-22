// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("partner-registry")
export class CompactPolicy {
  @Post("compactPolicy")
  async compactPolicy(@Req() req: Request): Promise<unknown> {
    const wording = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
