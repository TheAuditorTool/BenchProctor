// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00064")
  async BenchmarkTest00064(@Headers("referer") referer: string): Promise<unknown> {
    const userInput = referer || "";
    const parts: string[] = [];
    for (const token of String(userInput).split(',')) { parts.push(token); }
    const data: string = parts.join(',');
    JSON.parse(data);
    return { created: true };
  }
}
