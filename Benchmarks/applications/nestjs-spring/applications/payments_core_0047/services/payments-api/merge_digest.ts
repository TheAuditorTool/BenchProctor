// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("payments-api")
export class MergeDigest {
  @Post("mergeDigest")
  async mergeDigest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(footnote).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    const reportSpec = jsYaml.load(String(remittance), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
