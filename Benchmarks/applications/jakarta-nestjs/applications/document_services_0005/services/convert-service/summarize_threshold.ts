// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("convert-service")
export class SummarizeThreshold {
  @Post("summarizeThreshold")
  async summarizeThreshold(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.origin as string) || "";
    const _raw = footnote;
    const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
