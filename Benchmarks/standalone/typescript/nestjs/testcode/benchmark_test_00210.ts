// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Post, Query } from "@nestjs/common";
import { Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00210")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00210(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    const processed = isoDompurify.sanitize(marked.parse(data) as string);
    return "<div>" + processed + "</div>";
  }
}
