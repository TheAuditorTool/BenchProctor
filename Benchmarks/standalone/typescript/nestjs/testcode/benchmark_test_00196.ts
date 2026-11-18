// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00196")
  async BenchmarkTest00196(@Body("multipart_field") mf: string): Promise<unknown> {
    const userInput = mf || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    JSON.parse(data);
    return { created: true };
  }
}
