// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00143")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00143(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const _coerced = parseFloat(String(data));
    const parsedNum = _coerced;
    new Function("return (" + String(parsedNum) + ");")();
    return { created: true };
  }
}
